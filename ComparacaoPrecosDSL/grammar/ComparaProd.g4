grammar ComparaProd;

program: (comparison NEWLINE)* EOF;

comparison: 'compare' product (',' product)* NEWLINE?;

product: STRING 'de' quantity 'por' price promotion?;

quantity: NUMBER unit;

unit: 'ml' | 'l' | 'g' | 'kg' | 'oz';

price: 'R$' NUMBER;

promotion: 'com' NUMBER '% off';

STRING: '"' .*? '"';
NUMBER: [0-9]+ ('.' [0-9]+)?;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;