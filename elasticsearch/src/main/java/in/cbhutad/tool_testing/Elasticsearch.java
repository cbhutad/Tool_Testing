package in.cbhutad.tool_testing;

import java.io.IOException;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import co.elastic.clients.elasticsearch.ElasticsearchClient;

public class Elasticsearch {

    private static final Logger logger = LogManager.getLogger(Elasticsearch.class);
    private ElasticSearchConfig config = new ElasticSearchConfig();
    private ElasticsearchClient esClient = null;

    public void createIndex() throws IOException {
        esClient = config.createClient();
        esClient.indices().create(c -> c.index("categories"));
        System.out.println("Index created");
    }

}
