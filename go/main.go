package main

import "fmt"

type Message struct {
	key string
	value string
}

func main() {
	var mm = make(map[string]interface{})
	var m Message = Message{key: "key1", value: "value1"}

	mm["item1"] = m

	fmt.Println(m)
	fmt.Println(mm)
}