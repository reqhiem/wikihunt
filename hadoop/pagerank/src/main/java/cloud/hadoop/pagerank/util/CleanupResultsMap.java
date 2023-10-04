package cloud.hadoop.pagerank.util;

import cloud.hadoop.pagerank.RankRecord;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CleanupResultsMap extends
Mapper<LongWritable, Text, LongWritable, Text> {

    @Override
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {

        String strLine = value.toString();
        RankRecord rrObj = new RankRecord(strLine);

        context.write(new LongWritable(rrObj.sourceUrl),
                new Text(String.valueOf(rrObj.rankValue)));
    }

}
