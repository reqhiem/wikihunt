package cloud.hadoop.invertedindex;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class InvertedIndexMap extends Mapper<LongWritable, Text, Text, Text> {
    
    private Text word = new Text();

    @Override
    public void map(LongWritable key, Text value, Context context)
        throws IOException, InterruptedException {

            // Split DocID and the actual text
            String DocId = value.toString().substring(0, value.toString().indexOf("\t"));
            String value_raw = value.toString().substring(value.toString().indexOf("\t") + 1);

            // Reading input one line at a time and tokenizing by using space, "'", and "-" characters as tokenizers.
            StringTokenizer itr = new StringTokenizer(value_raw, " '-");

            // Iterating through all the words available in that line and forming the key/value pair.
            while (itr.hasMoreTokens()) {
                // Remove special characters
                word.set(itr.nextToken().replaceAll("[^a-zA-Z]", "").toLowerCase());
                if (word.toString() != "" && !word.toString().isEmpty()) {
                    context.write(word, new Text(DocId));
                }
            }
        }
}
