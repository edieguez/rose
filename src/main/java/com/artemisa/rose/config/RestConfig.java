package com.artemisa.rose.config;

import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration
public class RestConfig {
    private static final String DICT_API_URL = "https://api.dictionaryapi.dev/api/v2/entries";

    @Bean
    public RestTemplate freeDictionaryApiTemplate() {
        return new RestTemplateBuilder()
                .rootUri(DICT_API_URL)
                .build();
    }
}
