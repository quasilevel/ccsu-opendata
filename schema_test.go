package main

import (
	"encoding/json"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
	"regexp"
	"testing"
)

func TestSchema(t *testing.T) {
  pattern := regexp.MustCompile(`^[A-Z]+\/\d+\.json$`)

  filepath.WalkDir("./", func (path string, d fs.DirEntry, err error) error {
    if err != nil {
      return err
    }

    if !pattern.MatchString(path) {
      return nil
    }

    file, err := os.Open(path)
    if err != nil {
      return err
    }

    data := Data{}

    err = json.NewDecoder(file).Decode(&data)

    if err != nil {
      t.Fail()
      t.Log(fmt.Errorf("%s: syntax error in json: %w", path, err))
      return nil
    }

    if data.Title == "" {
      t.Fail()
      t.Logf("%s: title is missing", path)
    }

    if len(data.Topics) == 0 {
      t.Fail()
      t.Logf("%s: topic list is missing", path)
    } else {
      for idx, topic := range data.Topics {
        if topic.Name == "" {
          t.Fail()
          t.Logf("%s: topic name is missing for item at index %d", path, idx)
        }

        if len(topic.Weights) == 0 {
          t.Fail()
          t.Logf("%s: weight list is missing for item at index %d", path, idx)
        } else {
          for idxw, weight := range topic.Weights {
            if weight.Year < 2000 {
              t.Fail()
              t.Logf("%s: the year is invalid for item at %d/%d", path, idx, idxw)
            }

            if weight.Weight <= 0.0 {
              t.Fail()
              t.Logf("%s: the weight is invalid for item at %d/%d", path, idx, idxw)
            }
          }
        }
      }
    }

    return nil
  })
}
