package com.artemisa.rose.service.impl;

import com.artemisa.rose.mapper.FreeDictionaryMapper;
import com.artemisa.rose.model.Word;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class FreeDictionaryApi {

    private static final String WORD_DEFINITION_URL = "/{lang}/{word}";

    @Autowired
    private RestTemplate dictionaryApiTemplate;

    @Autowired
    private FreeDictionaryMapper freeDictionaryMapper;

    public Word getDefinition(String word, String lang) {
        return freeDictionaryMapper
                .map(dictionaryApiTemplate.getForObject(WORD_DEFINITION_URL, String.class, lang, word));
    }
}
