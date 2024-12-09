somaLista :: [Int] -> Int
somaLista [] = 0             
somaLista (x:xs) = x + somaLista xs 

main :: IO ()
main = do
    let vet = [1, 2, 3, 4, 5]
    putStrLn $ "A soma dos valores da lista e: " ++ show (somaLista vet)