package cloud.hadoop.pagerank;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class PageRankMap extends Mapper<LongWritable, Text, LongWritable, Text> {

    @Override
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {

        String line = value.toString();

        int numUrls = context.getConfiguration().getInt("numUrls", 1);

        RankRecord rrd = new RankRecord(line);

        if (rrd.targetUrlsList.size() <= 0) {
            double rankValuePerUrl = rrd.rankValue / numUrls;

            for (int i = 0; i < numUrls; i++) {
                context.write(new LongWritable(i), new Text(String.valueOf(rankValuePerUrl)));
            }

        }
        else {
            double rankValuePerUrl = (rrd.rankValue / rrd.targetUrlsList.size());

            for (int val : rrd.targetUrlsList) {
                context.write(new LongWritable(val), new Text(String.valueOf(rankValuePerUrl)));
            }

        }

        String mOut = "###" + line;
        context.write(new LongWritable(rrd.sourceUrl), new Text(mOut));

    }

}
