import React, { useState } from "react";
import {
  Input,
  Button,
  VStack,
  useToast,
  Heading,
  Box,
  FormControl,
  FormLabel,
} from "@chakra-ui/react";
import api from "../api";

export default function Deposit({ refreshAccounts }) {
  const [account, setAccount] = useState("");
  const [amount, setAmount] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const toast = useToast();

  const handleDeposit = async () => {
    if (isSubmitting) return; // prevent double click
    setIsSubmitting(true);

    try {
      await api.deposit(account, parseFloat(amount));

      toast({
        title: "Deposit successful!",
        status: "success",
        duration: 3000,
        isClosable: true,
      });

      setAccount("");
      setAmount("");

      if (refreshAccounts) refreshAccounts();

    } catch (err) {
      const msg =
        typeof err.response?.data === "object"
          ? err.response?.data?.msg || JSON.stringify(err.response.data)
          : err.response?.data || "Error";

      toast({
        title: "Deposit failed",
        description: msg,
        status: "error",
        duration: 4000,
        isClosable: true,
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Box p={5} borderWidth="1px" borderRadius="xl" boxShadow="md" bg="white">
      <Heading size="md" mb={4}>
        Deposit
      </Heading>
      <VStack spacing={3}>
        <FormControl>
          <FormLabel>Account Number</FormLabel>
          <Input
            value={account}
            onChange={(e) => setAccount(e.target.value)}
            placeholder="Enter account number"
          />
        </FormControl>

        <FormControl>
          <FormLabel>Amount</FormLabel>
          <Input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="Enter amount"
          />
        </FormControl>

        <Button
          colorScheme="green"
          onClick={handleDeposit}
          w="full"
          type="button"
          isLoading={isSubmitting}
          loadingText="Processing..."
          isDisabled={!account || !amount || isSubmitting}
        >
          Deposit
        </Button>
      </VStack>
    </Box>
  );
}
