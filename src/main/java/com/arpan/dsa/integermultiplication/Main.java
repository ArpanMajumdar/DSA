package com.arpan.dsa.integermultiplication;

import java.math.BigInteger;

public class Main {
  public static void main(String[] args) {
    //
    BigInteger x = new BigInteger("3141592653589793238462643383279502884197169399375105820974944592");
    BigInteger y = new BigInteger("2718281828459045235360287471352662497757247093699959574966967627");

    BigInteger expectedOutput = x.multiply(y);
    BigInteger actualOutput = KaratsubaDemo.karatsubaMultiplication(x, y);

    System.out.println("Actual product: " + x.multiply(y));
    System.out.println("Karatsuba product: " + KaratsubaDemo.karatsubaMultiplication(x, y));
    System.out.println(
        expectedOutput.equals(actualOutput)
            ? "Correct implementation"
            : "Incorrect implementation");
  }
}
