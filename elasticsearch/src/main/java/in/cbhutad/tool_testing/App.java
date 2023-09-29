package in.cbhutad.tool_testing;

import java.io.IOException;

/**
 * Hello world!
 *
 */
public class App {
    
    public static void main( String[] args ) throws IOException {
        Elasticsearch es = new Elasticsearch();
        es.createIndex();
        System.exit(0);
    }
}
