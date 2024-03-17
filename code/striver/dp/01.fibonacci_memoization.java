public class MyClass {

    private static int[] dp = new int[100];

    public static int fibonacci(int n) {
        if (n <= 1) {
            dp[n] = n;
            return n;
        }
        int fib_n_1 = 0;
        int fib_n_2 = 0;
        if (dp[n - 1] != -1) {
            fib_n_1 = dp[n - 1];
        } else {
            fib_n_1 = fibonacci(n - 1);
        }

        if (dp[n - 2] != -1) {
            fib_n_2 = dp[n - 2];
        } else {
            fib_n_2 = fibonacci(n - 2);
        }

        return dp[n] = fib_n_1 + fib_n_2; 
        // Store the result to dp[n] before return to this function
    }

    public static void main(String args[]) {
        for (int i = 0; i < 100; i++) {
            dp[i] = -1;
        }
        System.out.println(fibonacci(30));
    }
}