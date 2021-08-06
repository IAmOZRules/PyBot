import { Box, Flex, Heading, Input } from "@chakra-ui/react";
import { useRef, useState } from "react";
import BotMSG from "./components/BotMSG";
import UserMSG from "./components/UserMSG";

function App() {
  const [messages, setMessages] = useState([]);
  const userRef = useRef();

  const submitHandler = (e) => {
    e.preventDefault();
    const mess = userRef.current.value;
    fetch("http://127.0.0.1:8000/api/bot-response", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: mess }),
    })
      .then((resp) => resp.json())
      .then((jsonObj) => {
        console.log(jsonObj);
        setMessages((prev) => [...prev, { user: mess, bot: jsonObj }]);
        userRef.current.value = "";
      });
  };

  return (
    <Box
      bg="gray.400"
      h="33rem"
      w="60rem"
      mx="auto"
      mt="3rem"
      borderRadius="15px"
      boxShadow="2px 2px 8px gray"
      px="4.2rem"
      pt="0.9rem"
    >
      <Heading
        fontSize="1.8rem"
        fontFamily="body"
        pb="1.8rem"
        textAlign="center"
        textTransform="uppercase"
      >
        Your Messaging history
      </Heading>
      <Flex flexDir="column" overflowY="auto" alignItems="stretch" h="70%">
        <BotMSG text="Start with typing Hi!" />
        {messages.map((msg, idx) => (
          <Box key={idx}>
            <UserMSG text={msg.user} />
            <BotMSG text={msg.bot} />
          </Box>
        ))}
      </Flex>
      <Box position="relative">
        <Box w="100%" h="2px" bg="black"></Box>
        <form onSubmit={submitHandler}>
          <Input
            type="text"
            ref={userRef}
            _focus={{ bg: "gray.300" }}
            variant="filled"
            mt="1rem"
            placeholder="Enter your message"
          />
        </form>
      </Box>
    </Box>
  );
}

export default App;
