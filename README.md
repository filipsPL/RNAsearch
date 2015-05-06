# RNAsearch
Search for RNAs pairs: RNA apo -- RNA with ligand

## (PL)
jako dane wejściowe ma sekwencje z PDB (w naszym przypadku sekwencje RNA dla form apo i dla tych z ligandem małocząsteczkowym)
programik porównuje sekwencje z jednego pliku z drugim. Ma kilka opcji szukania (choć opcje to za dużo powiedziane - trzeba odkomentowywać odpowiednie linie kodu;) : identyczne sekwencje (także co do długości), identyczne, ale różnej długości oraz sekwencje podobne (proste porównywanie stringów met. pyhonową Ratcliff and Obershelp; właściwie można by zastosować jeszcze jakieś bardziej zaawansowane wyszukiwania, ale nie sądzę, żeby wyniki były znacząco różne)

no a jak już znajdzie to pobiera odpowiednie pliki z pdb do osobnych katalogów.

aha, te sekwencje w PDb trzeba wyszukać "ręcznie" ale nie jest to specjalnie uciążliwe. właściwie można by się pokusić o wrzucenie tego do skryptu, ale jako że jest to czynnośc jednorazowa to na razie niech zostanie tak, jak jest.
