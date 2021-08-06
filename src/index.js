import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { ChakraProvider, Box } from "@chakra-ui/react";
import Navbar from "./components/Navbar";

ReactDOM.render(
  <React.StrictMode>
    <ChakraProvider>
      <Box bg="#21ac7d" minH="100vh">
        <Navbar />
        <App />
      </Box>
    </ChakraProvider>
  </React.StrictMode>,
  document.getElementById("root")
);
