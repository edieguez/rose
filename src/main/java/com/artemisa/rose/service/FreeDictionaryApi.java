package com.artemisa.rose.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class FreeDictionaryApi {

    private static final String WORD_DEFINITION_URL = "/{lang}/{word}";

    @Autowired
    private RestTemplate dictionaryApiTemplate;

    public String getDefinition(String word, String lang) {
        return dictionaryApiTemplate.getForObject(WORD_DEFINITION_URL, String.class, lang, word);
    }
}
