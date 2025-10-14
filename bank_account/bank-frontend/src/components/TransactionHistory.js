import React, { useEffect, useState } from "react";
import { Box, Table, Thead, Tbody, Tr, Th, Td, Text } from "@chakra-ui/react";
import api from "../api";

export default function TransactionHistory() {
  const [transactions, setTransactions] = useState([]);

  const fetchTransactions = async () => {
    try {
      const res = await api.getTransactions(); // add this endpoint later
      setTransactions(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchTransactions();
  }, []);

  return (
    <Box>
      {transactions.length === 0 ? (
        <Text color="gray.500" textAlign="center">
          No transactions yet.
        </Text>
      ) : (
        <Table variant="simple" size="sm">
          <Thead>
            <Tr>
              <Th>Date</Th>
              <Th>Type</Th>
              <Th>Account</Th>
              <Th>Amount</Th>
              <Th>Status</Th>
            </Tr>
          </Thead>
          <Tbody>
            {transactions.map((tx) => (
              <Tr key={tx.id}>
                <Td>{new Date(tx.timestamp).toLocaleString()}</Td>
                <Td>{tx.type}</Td>
                <Td>{tx.account_number}</Td>
                <Td>₦{tx.amount.toLocaleString()}</Td>
                <Td>{tx.status}</Td>
              </Tr>
            ))}
          </Tbody>
        </Table>
      )}
    </Box>
  );
}
