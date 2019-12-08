package com.example.anlp.controller;

import com.example.anlp.util.DocumentFrequencyCounter;
import com.example.anlp.util.Summarizer;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.concurrent.ExecutionException;

@RestController
public class SummerizerController {

    @RequestMapping(value="/test", method = RequestMethod.POST)
    public String test() {
        return "Test";
    }
    @RequestMapping(value="/summarize", method = RequestMethod.POST)
    public ResponseEntity<String> summarize(@RequestParam("text") String text) throws InterruptedException, ExecutionException, IOException, ClassNotFoundException {
        System.out.println(text);
        DocumentFrequencyCounter.createDocumentSer("Tst");
        String input = Summarizer.getSummary();
        return new ResponseEntity<String>(input, HttpStatus.OK);
    }
}
