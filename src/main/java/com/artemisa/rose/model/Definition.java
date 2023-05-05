package com.artemisa.rose.model;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Setter
@NoArgsConstructor
@ToString
@JsonIgnoreProperties(ignoreUnknown = true)
public class Definition {
    private String partOfSpeech;
    private String definition;
    private String example;
}
