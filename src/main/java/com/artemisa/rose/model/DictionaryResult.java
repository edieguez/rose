package com.artemisa.rose.model;

import lombok.Builder;
import lombok.Getter;
import lombok.ToString;

@Builder
@Getter
@ToString
public class DictionaryResult {
    private String word;
    private String phonetic;
    private String imageUrl;
    private String audioUrl;
}
