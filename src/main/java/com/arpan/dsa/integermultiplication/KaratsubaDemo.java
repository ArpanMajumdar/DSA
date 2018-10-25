package com.arpan.dsa.integermultiplication;

import java.math.BigInteger;

public class KaratsubaDemo {
  public static final BigInteger TEN = BigInteger.TEN;

  public static BigInteger karatsubaMultiplication(BigInteger x, BigInteger y) {
    int m = x.toString().length();
    int n = y.toString().length();

    if (m == 1 || n == 1) {
      return x.multiply(y);
    } else {
      // x = 10^p * a + b
      // y = 10^q * c + d
      // x * y = [10^(p+q) * (a * c)] + [10^p * (a * d)] + [10^q * (b * c)] + [(b * d)]
      int p = m / 2;
      int q = n / 2;

      BigInteger[] xarr = x.divideAndRemainder(TEN.pow(p));
      BigInteger a = xarr[0];
      BigInteger b = xarr[1];

      BigInteger[] yarr = y.divideAndRemainder(TEN.pow(q));
      BigInteger c = yarr[0];
      BigInteger d = yarr[1];

      // Recursively compute a.c , a.d, b.c and b.d
      BigInteger term1 = TEN.pow(p + q).multiply(karatsubaMultiplication(a, c));
      BigInteger term2 = TEN.pow(p).multiply(karatsubaMultiplication(a, d));
      BigInteger term3 = TEN.pow(q).multiply(karatsubaMultiplication(b, c));
      BigInteger term4 = karatsubaMultiplication(b, d);

      return term1.add(term2).add(term3).add(term4);
    }
  }
}
