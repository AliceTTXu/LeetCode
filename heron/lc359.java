public class Logger {

    private Map<String, Integer> lastTime;
    private final int K = 10;

    /** Initialize your data structure here. */
    public Logger() {
        lastTime = new HashMap<String, Integer>();
    }

    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    public boolean shouldPrintMessage(int timestamp, String message) {

        if (lastTime.containsKey(message)) {
            int t = lastTime.get(message);
            if (timestamp - t >= K) {
                lastTime.put(message, timestamp);
                return true;
            }
            return false;
        }

        lastTime.put(message, timestamp);
        return true;

    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */
