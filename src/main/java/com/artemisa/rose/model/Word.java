package com.artemisa.rose.model;

import lombok.Builder;
import lombok.Getter;
import lombok.ToString;

import java.util.List;

@Builder
@Getter
@ToString
public class Word {
    private String word;
    private String phonetic;
    private String imageUrl;
    private String audioUrl;
    private List<Definition> definitions;
}
