package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Collections;
import java.util.Map;

@SpringBootApplication
@RestController
public class HelloWorldApplication {

	@GetMapping("/")
    public Map<String, String> helloWorld() {
        return Collections.singletonMap("hello", "world");
    }

	public static void main(String[] args) {
		SpringApplication.run(HelloWorldApplication.class, args);
	}
}
