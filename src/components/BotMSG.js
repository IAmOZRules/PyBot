import { Flex, Text } from "@chakra-ui/react";

const BotMSG = ({ text }) => {
  return (
    <Flex
      maxW="60%"
      py="0.4rem"
      px="1rem"
      color="white"
      borderRadius="10px"
      bg="blue.800"
      flexWrap="wrap"
      borderBottom="4px solid #e0e0e0"
    >
      <Text>{text}</Text>
    </Flex>
  );
};

export default BotMSG;
