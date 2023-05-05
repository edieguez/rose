package com.artemisa.rose.mapper;

import com.artemisa.rose.model.Definition;
import com.artemisa.rose.model.Word;
import com.jayway.jsonpath.DocumentContext;
import com.jayway.jsonpath.JsonPath;
import com.jayway.jsonpath.TypeRef;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

@Component
public class FreeDictionaryMapper {

    public Word map(String response) {
        DocumentContext context = JsonPath.parse(response);

        return Word.builder()
                .word(context.read("$[0].word"))
                .phonetic(context.read("$[0].phonetic"))
                .audioUrl(getAudioUrl(context))
                .definitions(getDefinitions(context))
                .build();
    }

    private String getAudioUrl(DocumentContext context) {
        List<String> audios = context.read("$[0].phonetics[?(@.audio)].audio", new TypeRef<>() {
        });

        return audios.isEmpty() ? null : audios.get(0);
    }

    private List<Definition> getDefinitions(DocumentContext context) {
        List<Definition> definitions = new ArrayList<>();
        Set<String> partsOfSpeech = context.read("$[*].meanings[*].partOfSpeech", new TypeRef<>() {
        });

        for (String partOfSpeech : partsOfSpeech) {
            definitions.addAll(getDefinitionByPartOfSpeech(context, partOfSpeech));
        }

        return definitions;
    }

    private List<Definition> getDefinitionByPartOfSpeech(DocumentContext context, String partOfSpeech) {
        List<Definition> definitions = context.read(String.format("$[*].meanings[?(@.partOfSpeech == '%s')].definitions[*]", partOfSpeech), new TypeRef<>() {
        });
        definitions.forEach(definition -> definition.setPartOfSpeech(partOfSpeech));

        return definitions;
    }
}
