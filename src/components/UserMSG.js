import { Flex, Text } from "@chakra-ui/react";

const UserMSG = ({ text }) => {
  return (
    <Flex
      w="60%"
      py="0.4rem"
      px="1rem"
      color="#2a4365"
      borderRadius="10px"
      bg="white"
      flexWrap="wrap"
      ml="auto"
      my="1rem"
      borderBottom="4px solid #2a4365"
    >
      <Text>{text}</Text>
    </Flex>
  );
};

export default UserMSG;
