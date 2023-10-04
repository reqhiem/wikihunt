package cloud.hadoop.pagerank;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class PageRankReduce extends
Reducer<LongWritable, Text, LongWritable, Text> {

    private final static double DampingFactor = 0.85;

    @Override
    public void reduce(LongWritable key, Iterable<Text> values, Context context)
            throws IOException, InterruptedException {

        double sumOfRankValues = 0.0;
        StringBuffer targetUrlsList = new StringBuffer("");

        int numUrls = context.getConfiguration().getInt("numUrls", 1);

        StringBuffer loggingString = new StringBuffer("");

        for (Text value : values) {

            String line = value.toString();
            loggingString.append(line);
            loggingString.append(",  ");

            if (line.contains("###")) {
                String normal = line.substring(3);
                RankRecord rrd = new RankRecord(normal);

                for (Integer eachTarget : rrd.targetUrlsList) {
                    targetUrlsList.append("#");
                    targetUrlsList.append(eachTarget);
                }

            } else {

                try {
                    sumOfRankValues += Double.parseDouble(value.toString());

                } catch (NumberFormatException nfe) {
                    sumOfRankValues += 0.0;
                    System.out.println("REDUCER WARN: bad rank values encountered!");
                }

            }

        }

        sumOfRankValues = (DampingFactor * sumOfRankValues + (1 - DampingFactor) * (1.0))  /  numUrls;
        context.write(key, new Text(sumOfRankValues + targetUrlsList.toString()));

    }

}
