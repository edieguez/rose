package com.artemisa.rose;

import com.artemisa.rose.service.impl.FreeDictionaryApi;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@Slf4j
@SpringBootApplication
public class RoseApplication implements CommandLineRunner {

    @Autowired
    private FreeDictionaryApi freeDictionaryApi;

    public static void main(String[] args) {
        SpringApplication.run(RoseApplication.class, args);
    }

    @Override
    public void run(String... args) {
        log.info("Definition: {}", freeDictionaryApi.getDefinition("rose", "en"));
    }
}
