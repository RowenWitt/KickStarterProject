package main

import (
	"encoding/json"
	"fmt"
	"os"
	"unsafe"
	"io/ioutil"
)

type Object struct {
	RunID string `json:"run_id"`
	Data  struct {
		ID                   int     `json:"id"`
		Name                 string  `json:"name"`
		Blurb                string  `json:"blurb"`
		Goal                 float32     `json:"goal"`
		Pledged              float32     `json:"pledged"`
		State                string  `json:"state"`
		Currency             string  `json:"currency"`
		Deadline             int     `json:"deadline"`
		StateChangedAt       int     `json:"state_changed_at"`
		CreatedAt            int     `json:"created_at"`
		LaunchedAt           int     `json:"launched_at"`
		BackersCount         int     `json:"backers_count"`
		StaticUSDRate        float32     `json:"static_usd_rate"`
		USDPledged           string `json:"usd_pledged"`
		ConvertPledgedAmount float32     `json:"convert_pledged_amount"`
		FXRate               float32     `json:"fx_rate"`
		CurrentCurrency      string  `json:"current_currency"`
		USDType              string  `json:"usd_type"`
		Creator              struct {
			Name string `json:"name"`
		} `json:"creator"`
		Location struct {
			ShortName string `json:"short_name"`
			Country   string `json:"country"`
			Type      string `json:"type"`
		} `json:"location"`
		Category struct {
			ID   int    `json:"id"`
			Slug string `json:"slug"`
		} `json:"category"`
		Profile struct {
			State          string `json:"state"`
			StateChangedAt int    `json:"state_changed_at"`
		} `json:"profile"`
	} `json:"data`
}

func LoadFile(path string) ([]*Object, error) {
	raw, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer raw.Close()

	val, err := ioutil.ReadAll(raw)
	if err != nil {
		return nil, err
	}

	var data []*Object
	err = json.Unmarshal(val, &data)
	if err != nil {
		return nil, err
	}

	return data, nil
}

func main() {
	data, err := LoadFile("listKick0.json")
	if err != nil {
		panic(err)
	}

	fmt.Println(data[0])
	fmt.Println("completed")
	fmt.Println(unsafe.Sizeof(data[0]), len(data))

	for {}
}
