package in.cbhutad.tool_testing;

import org.apache.http.HttpHost;
import org.elasticsearch.client.RestClient;
import co.elastic.clients.elasticsearch.ElasticsearchClient;
import co.elastic.clients.json.jackson.JacksonJsonpMapper;
import co.elastic.clients.transport.ElasticsearchTransport;
import co.elastic.clients.transport.rest_client.RestClientTransport;

public class ElasticSearchConfig {

    public static String url = "http://192.168.1.6:9200";

    public ElasticsearchClient createClient() {

        RestClient restClient = RestClient.builder(HttpHost.create(url)).build();
        ElasticsearchTransport transport = new RestClientTransport(restClient, new JacksonJsonpMapper());
        ElasticsearchClient elasticsearchClient = new ElasticsearchClient(transport);

        return elasticsearchClient;
    }
}