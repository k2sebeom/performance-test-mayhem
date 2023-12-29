package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

type HelloWorld struct {
	Hello string `json:"hello"`
}

func main() {
	// Create a new instance of Echo
	e := echo.New()

	// Route to handle HTTP GET requests at "/"
	e.GET("/", func(c echo.Context) error {
		return c.JSON(http.StatusOK, HelloWorld{
			Hello: "world",
		})
	})

	// Start the server on port 8080
	e.Logger.Fatal(e.Start(":8000"))
}
