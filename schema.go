package main

import (
	"encoding/json"
	"fmt"
	"reflect"

	"github.com/danielgtaylor/huma/schema"
)

type Weightage struct {
	Year   int `json:"year" doc:"Year when the topic appeared"`
  Weight float32 `json:"weight" doc:"Weight that the topic carried"`
}

type Topic struct {
	Name    string      `json:"name" doc:"Name of the topic"`
	Weights []Weightage `json:"weights" doc:"Year wise weightage of the topic"`
}

type Data struct {
	Title  string  `json:"title" doc:"The title of the subject"`
	Topics []Topic `json:"topics" doc:"An extensive list of topics that have appeared in the exams so far"`
}

func main() {
	s, err := schema.Generate(reflect.TypeOf(Data{}))
	if err != nil {
		panic(err)
	}

	b, err := json.MarshalIndent(s, "", "  ")
	if err != nil {
		panic(err)
	}

	fmt.Println(string(b))
}

