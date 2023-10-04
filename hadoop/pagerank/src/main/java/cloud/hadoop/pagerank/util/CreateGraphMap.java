package cloud.hadoop.pagerank.util;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CreateGraphMap extends
Mapper<LongWritable, Text, LongWritable, Text> {

    @Override
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {

        String[] strArray = value.toString().split(" ");

        int sourceUrl;
        sourceUrl = Integer.parseInt(strArray[0]);

        int numUrls = context.getConfiguration().getInt("numUrls", 1);
        double initialWeight = 1.0 / numUrls;

        StringBuffer stringBufferObj = new StringBuffer();
        stringBufferObj.append(String.valueOf(initialWeight));

        int targetUrl;
        for (int i = 1; i < strArray.length; i++) {
            targetUrl = Integer.parseInt(strArray[i]);
            stringBufferObj.append("#" + targetUrl);
        }

        context.write(new LongWritable(sourceUrl),
                new Text(stringBufferObj.toString()));

    }
}
