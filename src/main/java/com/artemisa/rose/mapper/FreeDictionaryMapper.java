package com.artemisa.rose.mapper;

import com.artemisa.rose.model.DictionaryResult;
import com.jayway.jsonpath.DocumentContext;
import com.jayway.jsonpath.JsonPath;
import com.jayway.jsonpath.TypeRef;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class FreeDictionaryMapper {

    public DictionaryResult map(String response) {
        DocumentContext context = JsonPath.parse(response);

        return DictionaryResult.builder()
                .word(context.read("$[0].word"))
                .phonetic(context.read("$[0].phonetic"))
                .audioUrl(getAudioUrl(context))
                .build();
    }

    private String getAudioUrl(DocumentContext context) {
        List<String> audios = context.read("$[0].phonetics[?(@.audio)].audio", new TypeRef<>() {
        });

        return audios.isEmpty() ? null : audios.get(0);
    }
}
