import React, { useEffect, useState } from 'react';
import { Box, Heading, Table, Thead, Tr, Th, Td, Tbody } from '@chakra-ui/react';
import api from '../api';

export default function AccountList() {
  const [accounts, setAccounts] = useState([]);

  const fetchAccounts = async () => {
    const response = await api.getAccounts();
    setAccounts(response.data);
  };

  useEffect(() => {
    fetchAccounts();
  }, []);

  return (
    <Box p={4}>
      <Heading size="md" mb={4}>Accounts</Heading>
      <Table variant="simple">
        <Thead>
          <Tr>
            <Th>Account Number</Th>
            <Th>First Name</Th>
            <Th>Last Name</Th>
            <Th>Balance</Th>
          </Tr>
        </Thead>
        <Tbody>
          {accounts.map((acc) => (
            <Tr key={acc.account_number}>
              <Td>{acc.account_number}</Td>
              <Td>{acc.first_name}</Td>
              <Td>{acc.last_name}</Td>
              <Td>{acc.balance}</Td>
            </Tr>
          ))}
        </Tbody>
      </Table>
    </Box>
  );
}
