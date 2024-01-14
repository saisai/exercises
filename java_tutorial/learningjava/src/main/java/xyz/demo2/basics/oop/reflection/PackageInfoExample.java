package xyz.demo2.basics.oop.reflection;

public class PackageInfoExample {
    public static void main(String[] args) {
        // 1. Get a reference to a class within the package you want to inspect.
        // For example, we'll use this class itself.
        Class<?> clazz = PackageInfoExample.class;

        // 2. Get the package information for the class.
        Package pkg = clazz.getPackage();

        // 3. Access package-related information.
        String packageName = pkg.getName();
        String specificationVersion = pkg.getSpecificationVersion();
        String implementationVersion = pkg.getImplementationVersion();

        // Display the package information.
        System.out.println("Package Name: " + packageName);
        System.out.println("Specification Version: " + specificationVersion);
        System.out.println("Implementation Version: " + implementationVersion);
    }
}
