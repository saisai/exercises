import zlib, base64

b64 = b'''
eNrtVE1rwzAMvedXaKdeRn7ENrb21rHCzmrs1m49K9gOJv9+cko/HBcGg0LHcpOfnq2np0QL
2FuKgBbICDAoeoiKwEc0hqIUgLAxfV0tQJCdhQM7qh68kheswKeBt5ROYetTemYMCC3rii//
WMS3WkhXVyuFAaLT261JuBWwu4iDbvYp1tYzHVS68VEIObwFgaDB0KizuFs38aSdqKv3TgcJ
uPYdn2B1opwIpeKE53qPftxRd88Y6uoVbdPzWxznrQ3ZUi3DudQ/bcELbevqM32iCIrj3IIh
W6plOJf6L6xaajZjzqW/qAsKIvITBGs9Nm3glboZzkVP5l6Y+0bHLnedD0CttIyrpEU5Kv7N
Mz3XkPBc/TSN3yxGiqMiipHRekycK0ZwMhM8jerGC9zuZaoTho3kMKSfJjLaF8v8wLzmXMqM
zJvGew/jnZPzclA08yAkikegDTTUMfzwDXBcwoE='''
#print(zlib.decompress(base64.b64decode(b64)).decode("utf-8", "strict"))

animals = [
        ("fly", "I don't know why she swallowed a fly, perhaps she'll die."),
        ("spider", "It wiggled and jiggled and tickled inside her."),
        ("bird", "How absurd, to swallow a bird."),
        ("cat", "Imagine that, she swallowed a cat."),
        ("dog", "What a hog, to swallow a dog."),
        ("goat", "She just opened her throat and swallowed a goat."),
        ("cow", "I don't know how she swallowed a cow."),
        ("horse", "She's dead, of course.")]

for i, (animal, lyric) in enumerate(animals):
    print( "There was an old lady who swallowed a {}.\n{}".format(animal, lyric))

    if animal == "horse": break

    for(predator, _), (prey, _) in zip(animals[i:0:-1], animals[i-1::-1]):
        print("\tShe swallowed the {} to catch the {}".format(predator, prey))

    if animal != "fly": print(animals[0][1]) # fly lyric
    print()
