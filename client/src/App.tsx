import { useState } from 'react';
import './App.css';
import {
    Input,
    Box,
    Container,
    Button,
    Flex,
    Heading,
    Text,
} from '@chakra-ui/react';
import axios from 'axios';

type IResult = {
    id: string;
    title: string;
    url: string;
    hash: string;
};

function App() {
    const [search, setSearch] = useState('');
    const [results, setResults] = useState<IResult[]>([]);
    const handleInput = (e: React.ChangeEvent<HTMLInputElement>) => {
        setSearch(e.target.value);
    };

    const handleSubmit = () => {
        axios
            .get('http://localhost:5000/api/search', {
                params: {
                    query: search,
                },
            })
            .then((res) => {
                setResults(res.data.results);
            });
    };
    return (
        <>
            <Box px={10} my={10}>
                <Container maxW="container.md">
                    <Heading as="h1" size="2xl" className="font-mono">
                        <span className="text-sky-500	">Wiki</span>
                        <span className="text-gray-400">Hunt</span>
                    </Heading>
                    <Flex gap={2} my={4}>
                        <Input type="search" onChange={handleInput} />
                        <Button onClick={handleSubmit}>Search</Button>
                    </Flex>
                    <Text className="text-sm text-gray-600" my={4} p={1}>
                        Se muestran {results.length} resultados
                    </Text>
                    <Box>
                        {results.map((item, index) => (
                            <Box
                                key={index}
                                my={2}
                                rounded="md"
                                shadow="lg"
                                p={3}
                            >
                                <Heading size="md">{item.title}</Heading>
                                <a
                                    href={item.url}
                                    target="_blank"
                                    rel="noreferrer"
                                    className="text-blue-400 text-sm"
                                >
                                    {item.url}
                                </a>
                            </Box>
                        ))}
                    </Box>
                </Container>
            </Box>
        </>
    );
}

export default App;
