package com.artemisa.rose.service;

import com.artemisa.rose.model.DictionaryResult;

public interface DictionaryService {
    DictionaryResult getDefinition(String word, String lang);
}
