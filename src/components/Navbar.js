import { Flex, Heading } from "@chakra-ui/react";

const Navbar = () => {
  return (
    <Flex
      w="100vw"
      bg="black"
      h="10vh"
      alignItems="center"
      justifyContent="center"
      //boxShadow="2px 2px 8px green"
    >
      <Heading
        colorScheme="whiteAlpha"
        color="red.500"
        fontFamily="fantasy"
        letterSpacing="0.4rem"
      >
        PyBot
      </Heading>
    </Flex>
  );
};

export default Navbar;
