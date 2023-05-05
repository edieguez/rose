package com.artemisa.rose.service;

import com.artemisa.rose.model.Word;

public interface DictionaryService {
    Word getDefinition(String word, String lang);
}
