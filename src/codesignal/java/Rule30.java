package test;

import java.math.BigInteger;

public class Rule30 {

  public static void main(String[] args) {
    Rule30 r = new Rule30();
    System.out.println(r.rule30(41));
  }

  int rule30(int n) {
    BigInteger b = new BigInteger("1");
    
    for (int i = 0; i < n; i++)
      b = b.xor(b.multiply(new BigInteger("2")).or(b.multiply(new BigInteger("4"))));
     
    return b.bitCount();
  }
}
