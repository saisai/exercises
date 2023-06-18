package com.mycompany.github.douglascraigschmidt.LiveLessons.Java8.ex8.utils;

import java.util.*;
import java.util.concurrent.CompletableFuture;
import java.util.function.BiConsumer;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.Supplier;
import java.util.stream.Collector;

import static java.util.stream.Collectors.toList;

public class FuturesCollector<T> implements Collector<CompletableFuture<T>,
        List<CompletableFuture<T>>,
        CompletableFuture<List<T>>> {

    @Override
    public Supplier<List<CompletableFuture<T>>> supplier() {
        return ArrayList::new;
    }

    @Override
    public BiConsumer<List<CompletableFuture<T>>, CompletableFuture<T>> accumulator() {
        return Collection::add;
    }

    @Override
    public BinaryOperator<List<CompletableFuture<T>>> combiner() {
        return (List<CompletableFuture<T>> one,
                List<CompletableFuture<T>> another) -> {
            one.addAll(another);
            return one;
        };
    }

    @Override
    public Function<List<CompletableFuture<T>>, CompletableFuture<List<T>>>
    finisher() {
        return futures -> CompletableFuture
                // Use CompletableFuture.allOf() to obtain a future that
                // will itself be complete when all futures complete.
                .allOf(futures.toArray(new CompletableFuture[0]))

                // When all futures have completed get a single future to
                // a list of joined elements of type T.
                .thenApply(v -> futures
                        // Convert futures into a stream of completable
                        // futures.
                        .stream()

                        // Use map() to join() all completable futures
                        // and yield objects of type T.  Note that
                        // join() should never block.
                        .map(CompletableFuture::join)

                        // Collect the results of type T into a list.
                        .toList());
    }

    @Override
    public Set<Characteristics> characteristics() {
        return Collections.singleton(Characteristics.UNORDERED);
    }

    public static <T> Collector<CompletableFuture<T>, ?, CompletableFuture<List<T>>>
    toFuture() {
        return new FuturesCollector<T>();
    }


}
