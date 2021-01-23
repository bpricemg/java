/**
 * Tests the object, Pet
 *
 */

class PetTest
{
    public static void main(String[] args)
    {
        // Creates variables of type pet with different constructors
        Pet myDog = new Pet ("Fido", 9, 29.5);
        Pet myParrot = new Pet ("Polly", 32, 2.85);
        Pet myCat = new Pet ("Tiger", 4);

        // Prints out the name with an instance method
        System.out.println(myDog.getName());
        System.out.println(myParrot.getName());
        System.out.println(myCat.getName());
    }
}
