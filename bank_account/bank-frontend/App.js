import React from "react";
import {
  ChakraProvider,
  Box,
  Grid,
  GridItem,
  Heading,
  VStack,
  extendTheme,
} from "@chakra-ui/react";

import CreateAccount from "./components/CreateAccount";
import Deposit from "./components/Deposit";
import Withdraw from "./components/Withdraw";
import Transfer from "./components/Transfer";
import AccountList from "./components/AccountList";
import TransactionHistory from "./components/TransactionHistory";


const theme = extendTheme({
  colors: {
    brand: {
      100: "#E6FFFA",
      500: "#319795",
      700: "#285E61",
    },
  },
});

export default function App() {
  return (
    <ChakraProvider theme={theme}>
      <Box bg="gray.50" minH="100vh" p={6}>
        <Heading mb={6} color="teal.700" textAlign="center">
          🏦 SmartBank Dashboard
        </Heading>

        <Grid
          templateColumns={{ base: "1fr", md: "repeat(2, 1fr)", xl: "repeat(3, 1fr)" }}
          gap={6}
        >
          <GridItem>
            <CardBox title="Create Account">
              <CreateAccount />
            </CardBox>
          </GridItem>

          <GridItem>
            <CardBox title="Deposit Funds">
              <Deposit />
            </CardBox>
          </GridItem>

          <GridItem>
            <CardBox title="Withdraw Funds">
              <Withdraw />
            </CardBox>
          </GridItem>

          <GridItem>
            <CardBox title="Transfer Funds">
              <Transfer />
            </CardBox>
          </GridItem>

          <GridItem colSpan={{ base: 1, md: 2, xl: 3 }}>
            <CardBox title="Accounts">
              <AccountList />
            </CardBox>
          </GridItem>

          <GridItem colSpan={{ base: 1, md: 2, xl: 3 }}>
            <CardBox title="Transaction History">
              <TransactionHistory />
            </CardBox>
          </GridItem>
        </Grid>
      </Box>
    </ChakraProvider>
  );
}


function CardBox({ title, children }) {
  return (
    <Box
      bg="white"
      p={5}
      rounded="2xl"
      shadow="md"
      border="1px solid"
      borderColor="gray.100"
      _hover={{ shadow: "lg", transform: "scale(1.01)", transition: "0.2s" }}
    >
      <VStack align="stretch" spacing={4}>
        <Heading size="sm" color="teal.600" textAlign="center">
          {title}
        </Heading>
        {children}
      </VStack>
    </Box>
  );
}
