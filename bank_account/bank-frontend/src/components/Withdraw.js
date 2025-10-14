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

export default function Withdraw({ refreshAccounts }) {
  const [account, setAccount] = useState("");
  const [amount, setAmount] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const toast = useToast();

  const handleWithdraw = async () => {
    if (isSubmitting) return;
    setIsSubmitting(true);
    try {
      await api.withdraw(account, parseFloat(amount));
      toast({ title: "Withdrawal successful!", status: "success", duration: 3000, isClosable: true });
      setAccount("");
      setAmount("");
      refreshAccounts?.();
    } catch (err) {
      const msg =
        typeof err.response?.data === "object"
          ? err.response?.data?.msg || JSON.stringify(err.response.data)
          : err.response?.data || "Error";
      toast({ title: "Withdrawal failed", description: msg, status: "error", duration: 4000, isClosable: true });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Box p={5} borderWidth="1px" borderRadius="xl" boxShadow="md" bg="white">
      <Heading size="md" mb={4}>Withdraw</Heading>
      <VStack spacing={3}>
        <FormControl>
          <FormLabel>Account Number</FormLabel>
          <Input value={account} onChange={(e) => setAccount(e.target.value)} />
        </FormControl>
        <FormControl>
          <FormLabel>Amount</FormLabel>
          <Input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} />
        </FormControl>
        <Button type="button" colorScheme="red" onClick={handleWithdraw} w="full" isLoading={isSubmitting}>Withdraw</Button>
      </VStack>
    </Box>
  );
}
