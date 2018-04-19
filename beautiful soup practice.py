import json
import requests
from pprint import pprint
import collections
import xlsxwriter
import xlrd
url = 'http://exac.hms.harvard.edu/rest/gene/variants_in_gene/ENSG00000049656'
response = requests.get(url)
response.raise_for_status()
data = json.loads(response.text)
b = {'5-1325974-G-A': '2.2e-05 (South Asian)', '5-1323052-C-G': '0 (None)', '5-1321856-G-A': '3.4e-05 (African)', '5-1335136-G-A': '0.000242 (Latino)', '5-1335304-C-T': '0 (None)', '5-1330374-A-T': '0 (None)', '5-1323033-C-T': '0 (None)', '5-1324863-T-A': '0 (None)', '5-1341876-C-G': '0 (None)', '5-1335227-C-T': '0 (None)', '5-1323052-C-T': '0 (None)', '5-1331975-A-G': '0 (None)', '5-1321928-T-C': '0 (None)', '5-1341758-G-C': '0 (None)', '5-1341936-A-G': '2.1e-05 (South Asian)', '5-1334387-C-A': '0 (None)', '5-1323875-G-C': '0 (None)', '5-1344501-A-T': '0 (None)', '5-1324916-T-C': '3.4e-05 (African)', '5-1338034-G-A': '2e-05 (European (Non-Finnish))', '5-1321762-G-A': '0 (None)', '5-1321731-C-T': '2.1e-05 (South Asian)', '5-1323891-C-T': '8e-05 (African)', '5-1335148-G-T': '0 (None)', '5-1321966-CGGAGGGCCGGGCTGCCACATCTACGCACAGACGGCACTCACGAGGTGT-C': '0 (None)', '5-1334373-C-T': '0 (None)', '5-1344798-C-T': '4.6e-05 (South Asian)', '5-1338055-G-A': '0 (None)', '5-1344512-G-A': '0 (None)', '5-1325953-T-C': '3e-05 (Latino)', '5-1335254-G-T': '0 (None)', '5-1338949-C-T': '0.000558 (African)', '5-1320786-G-A': '0 (None)', '5-1335321-C-T': '0 (None)', '5-1323947-C-G': '0 (None)', '5-1334384-C-G': '0.000758 (South Asian)', '5-1330529-G-A': '0 (None)', '5-1344972-G-A': '0.000822 (South Asian)', '5-1334547-T-C': '3.3e-05 (European (Non-Finnish))', '5-1320709-G-A': '0 (None)', '5-1330345-C-G': '5e-06 (European (Non-Finnish))', '5-1341992-A-G': '0 (None)', '5-1334389-C-T': '0 (None)', '5-1323033-C-CG': '0 (None)', '5-1338945-C-G': '0.001726 (African)', '5-1334534-G-A': '5e-06 (European (Non-Finnish))', '5-1321798-A-C': '7e-05 (Latino)', '5-1335123-G-A': '0 (None)', '5-1344850-C-G': '0 (None)', '5-1324834-G-C': '0 (None)', '5-1341889-G-A': '3e-05 (Latino)', '5-1325913-C-CAGACACCATGGCCTGCGTCAGCTGCCTGGCGAATGTGA': '0 (None)', '5-1320793-C-T': '0 (None)', '5-1330355-C-T': '3e-05 (Latino)', '5-1318481-C-T': '3e-05 (Latino)', '5-1334472-C-T': '7.8e-05 (African)', '5-1321960-G-A': '0.006916 (European (Non-Finnish))', '5-1322966-T-G': '4.1e-05 (East Asian)', '5-1335244-C-T': '0 (None)', '5-1331967-T-C': '0 (None)', '5-1344589-A-G': '0 (None)', '5-1334507-GA-G': '0.8027 (East Asian)', '5-1335310-G-A': '0 (None)', '5-1325967-T-C': '0.000122 (South Asian)', '5-1321699-G-A': '0 (None)', '5-1337995-C-G': '0 (None)', '5-1344493-T-C': '0 (None)', '5-1344578-G-A': '1.2e-05 (European (Non-Finnish))', '5-1341896-C-T': '0 (None)', '5-1318598-A-C': '5e-06 (European (Non-Finnish))', '5-1334415-C-T': '0 (None)', '5-1344744-G-GGA': '0 (None)', '5-1337980-T-TCCCCC': '0.01048 (African)', '5-1334507-GAA-G': '5.1e-05 (European (Non-Finnish))', '5-1335253-C-T': '5e-06 (European (Non-Finnish))', '5-1324007-C-T': '0 (None)', '5-1334387-C-T': '0.000199 (South Asian)', '5-1321804-G-T': '4.9e-05 (South Asian)', '5-1344524-T-C': '0 (None)', '5-1323940-C-T': '0 (None)', '5-1338135-G-C': '0 (None)', '5-1330413-A-C': '0.000584 (European (Non-Finnish))', '5-1321845-G-A': '0.000597 (African)', '5-1325834-C-T': '0.000468 (Latino)', '5-1339058-C-T': '1.2e-05 (European (Non-Finnish))', '5-1335197-G-A': '0.000118 (Latino)', '5-1334415-C-A': '0 (None)', '5-1318499-C-T': '1.2e-05 (European (Non-Finnish))', '5-1324896-G-C': '0 (None)', '5-1331903-G-A': '0 (None)', '5-1337980-T-TCCCCCCC': '0.00859 (African)', '5-1337985-A-C': '0.01845 (African)', '5-1325940-A-G': '0 (None)', '5-1331965-T-C': '0 (None)', '5-1334411-G-A': '0.000119 (South Asian)', '5-1341946-G-C': '8.5e-05 (South Asian)', '5-1332016-G-A': '0 (None)', '5-1324838-T-C': '0 (None)', '5-1344933-G-A': '0.000135 (South Asian)', '5-1331956-A-G': '0 (None)', '5-1320770-C-T': '0 (None)', '5-1339006-G-A': '0 (None)', '5-1324014-G-A': '0 (None)', '5-1344517-A-T': '3e-05 (European (Non-Finnish))', '5-1339101-T-G': '0 (None)', '5-1344498-C-G': '0.006437 (African)', '5-1320688-C-T': '0 (None)', '5-1318461-G-A': '1.2e-05 (European (Non-Finnish))', '5-1339016-G-A': '0.000241 (South Asian)', '5-1332040-T-C': '4.6e-05 (East Asian)', '5-1337987-C-T': '4.2e-05 (South Asian)', '5-1335153-G-A': '0 (None)', '5-1338101-G-A': '0 (None)', '5-1338964-G-T': '0.01453 (African)', '5-1320722-C-T': '0.4574 (African)', '5-1325830-G-A': '0 (None)', '5-1335144-C-T': '0.002059 (African)', '5-1330378-C-T': '0 (None)', '5-1344824-G-A': '0.00011 (European (Non-Finnish))', '5-1323922-G-A': '1.2e-05 (European (Non-Finnish))', '5-1344846-G-A': '0 (None)', '5-1341946-G-A': '4e-05 (European (Non-Finnish))', '5-1321944-G-C': '0 (None)', '5-1334363-C-G': '0 (None)', '5-1335326-T-C': '0 (None)', '5-1330469-T-A': '0 (None)', '5-1338035-C-T': '0.000142 (Latino)', '5-1325851-A-G': '0 (None)', '5-1334533-G-A': '0 (None)', '5-1334516-AC-A': '0.000138 (African)', '5-1338007-G-A': '1.4e-05 (European (Non-Finnish))', '5-1321739-G-A': '9.4e-05 (East Asian)', '5-1335330-CTT-C': '0 (None)', '5-1332027-A-G': '0 (None)', '5-1335138-C-T': '5e-06 (European (Non-Finnish))', '5-1321951-AGCACTCACGAGGTGCGGAGGGCCGGGCTGCCACATCTACGCACAGACG-A': '0 (None)', '5-1339042-C-G': '0 (None)', '5-1323034-G-A': '0.007296 (African)', '5-1337988-T-C': '0 (None)', '5-1338990-T-C': '0 (None)', '5-1344804-G-A': '0 (None)', '5-1320738-G-A': '0 (None)', '5-1335269-G-C': '0.00012 (South Asian)', '5-1324884-A-G': '0 (None)', '5-1335152-C-T': '0.001804 (East Asian)', '5-1344525-C-G': '0 (None)', '5-1334473-C-T': '0 (None)', '5-1321843-C-T': '0.00499 (African)', '5-1323920-A-G': '4.9e-05 (European (Non-Finnish))', '5-1334378-G-A': '6e-05 (European (Non-Finnish))', '5-1321923-A-G': '0 (None)', '5-1335163-G-A': '0 (None)', '5-1321858-G-A': '2.1e-05 (South Asian)', '5-1325941-G-A': '1.2e-05 (European (Non-Finnish))', '5-1334434-C-A': '0 (None)', '5-1321942-A-C': '2.3e-05 (South Asian)', '5-1321808-G-A': '0 (None)', '5-1334383-G-GC': '0.000118 (Latino)', '5-1323886-G-A': '9.5e-05 (East Asian)', '5-1335295-G-C': '0 (None)', '5-1344848-A-G': '0.001991 (European (Non-Finnish))', '5-1335268-C-T': '2.1e-05 (South Asian)', '5-1339143-G-A': '6e-06 (European (Non-Finnish))', '5-1339144-C-T': '0 (None)', '5-1321955-C-G': '0.000494 (East Asian)', '5-1324852-C-T': '5e-06 (European (Non-Finnish))', '5-1334506-G-A': '7e-06 (European (Non-Finnish))', '5-1335160-T-C': '0 (None)', '5-1338033-C-T': '0 (None)', '5-1330418-C-A': '0 (None)', '5-1323059-C-A': '0.000138 (European (Non-Finnish))', '5-1323045-G-A': '5e-06 (European (Non-Finnish))', '5-1324896-G-A': '0 (None)', '5-1334362-C-T': '0 (None)', '5-1341810-C-T': '5e-06 (European (Non-Finnish))', '5-1335156-C-T': '0 (None)', '5-1344843-G-C': '0 (None)', '5-1330488-G-A': '9.5e-05 (East Asian)', '5-1334361-G-GC': '5e-06 (European (Non-Finnish))', '5-1330517-G-C': '0 (None)', '5-1324965-CAG-C': '7e-05 (Latino)', '5-1331890-C-G': '0 (None)', '5-1318500-G-A': '2.9e-05 (European (Non-Finnish))', '5-1335269-G-T': '0 (None)', '5-1321940-G-A': '6e-06 (European (Non-Finnish))', '5-1321843-C-CG': '0 (None)', '5-1325838-G-A': '0 (None)', '5-1338033-C-G': '0 (None)', '5-1330375-G-C': '0 (None)', '5-1335209-G-A': '5e-06 (European (Non-Finnish))', '5-1320829-A-G': '0 (None)', '5-1318552-T-C': '0 (None)', '5-1334539-G-A': '0 (None)', '5-1342010-T-C': '3.2e-05 (European (Non-Finnish))', '5-1323872-G-A': '5e-06 (European (Non-Finnish))', '5-1341864-G-A': '0 (None)', '5-1318490-C-T': '0.000228 (East Asian)', '5-1321825-T-C': '0.000131 (African)', '5-1330386-G-T': '0 (None)', '5-1321966-C-T': '2.6e-05 (South Asian)', '5-1334389-C-A': '4.9e-05 (South Asian)', '5-1339015-C-T': '0 (None)', '5-1321735-G-A': '8.2e-05 (South Asian)', '5-1335225-C-A': '0 (None)', '5-1334385-C-A': '3e-05 (Latino)', '5-1341775-A-G': '0 (None)', '5-1334447-T-C': '0.000118 (Latino)', '5-1321873-C-T': '0.1782 (European (Non-Finnish))', '5-1330379-A-G': '0 (None)', '5-1341818-T-C': '4.9e-05 (South Asian)', '5-1341945-C-T': '0 (None)', '5-1334386-C-A': '0 (None)', '5-1334497-C-A': '0 (None)', '5-1321975-G-A': '8e-06 (European (Non-Finnish))', '5-1344512-G-C': '0 (None)', '5-1341881-C-T': '0 (None)', '5-1334504-A-G': '0 (None)', '5-1341863-G-T': '0 (None)', '5-1330460-A-T': '3.4e-05 (African)', '5-1344835-T-C': '0.001043 (East Asian)', '5-1335254-G-A': '0 (None)', '5-1341878-C-T': '4.9e-05 (South Asian)', '5-1330492-C-G': '3e-05 (Latino)', '5-1341825-T-G': '0.000159 (South Asian)', '5-1341831-G-A': '0 (None)', '5-1325842-T-A': '9.4e-05 (East Asian)', '5-1337980-T-TCCCCCCCC': '0.01407 (African)', '5-1338074-T-C': '0 (None)', '5-1334383-GC-G': '0.000562 (South Asian)', '5-1331887-G-A': '0 (None)', '5-1335185-G-A': '0.000533 (African)', '5-1330355-C-A': '0 (None)', '5-1334481-C-G': '0 (None)', '5-1318503-C-T': '3.4e-05 (African)', '5-1318535-C-T': '0 (None)', '5-1344889-G-A': '0 (None)', '5-1324895-C-T': '1.2e-05 (European (Non-Finnish))', '5-1323035-G-GA': '0.01662 (European (Non-Finnish))', '5-1322954-A-G': '0 (None)', '5-1324971-G-A': '0.001216 (Latino)', '5-1331881-G-A': '0 (None)', '5-1341812-G-A': '0.000379 (East Asian)', '5-1330494-G-C': '0 (None)', '5-1335225-C-T': '4.9e-05 (South Asian)', '5-1320708-C-T': '0 (None)', '5-1335269-G-A': '5e-06 (European (Non-Finnish))', '5-1321940-GAA-G': '0 (None)', '5-1318548-C-T': '0 (None)', '5-1324974-T-C': '0 (None)', '5-1331918-C-A': '9.4e-05 (East Asian)', '5-1344779-C-G': '0 (None)', '5-1341953-T-C': '0.00401 (South Asian)', '5-1344537-G-A': '4.1e-05 (East Asian)', '5-1341793-T-G': '7.8e-05 (African)', '5-1337986-G-C': '0.01208 (African)', '5-1318519-C-T': '0 (None)', '5-1321703-A-C': '0 (None)', '5-1330385-C-T': '0 (None)', '5-1344555-G-A': '0 (None)', '5-1341839-T-C': '1.2e-05 (European (Non-Finnish))', '5-1325856-T-A': '0 (None)', '5-1338095-A-G': '6.4e-05 (East Asian)', '5-1338088-C-G': '0 (None)', '5-1321937-G-A': '0.000129 (South Asian)', '5-1323072-A-G': '0 (None)', '5-1341831-G-T': '0 (None)', '5-1318478-C-T': '0.000695 (African)', '5-1344606-C-A': '0.000599 (South Asian)', '5-1324976-T-C': '0 (None)', '5-1335279-C-T': '0 (None)', '5-1318474-C-T': '0 (None)', '5-1334367-C-G': '0 (None)', '5-1341910-A-G': '0 (None)', '5-1321704-C-A': '0 (None)', '5-1338011-T-C': '0 (None)', '5-1325939-G-T': '0 (None)', '5-1334466-C-G': '2e-05 (European (Non-Finnish))', '5-1335140-T-C': '0 (None)', '5-1334521-C-T': '8.5e-05 (South Asian)', '5-1341945-C-G': '5e-06 (European (Non-Finnish))', '5-1330417-G-A': '0 (None)', '5-1321927-A-G': '0 (None)', '5-1322970-G-A': '3.9e-05 (European (Non-Finnish))', '5-1330344-G-A': '0 (None)', '5-1321812-G-A': '0 (None)', '5-1330430-C-A': '8e-05 (African)', '5-1321782-C-A': '3e-05 (Latino)', '5-1344495-T-C': '0 (None)', '5-1318559-A-C': '0 (None)', '5-1331922-G-C': '2.1e-05 (South Asian)', '5-1334442-A-G': '0 (None)', '5-1337981-C-T': '0.0001 (African)', '5-1331957-G-A': '0 (None)', '5-1341761-A-C': '0.00011 (South Asian)', '5-1322942-G-C': '0 (None)', '5-1332020-G-A': '0 (None)', '5-1335132-G-A': '0 (None)', '5-1330475-C-T': '5e-06 (European (Non-Finnish))', '5-1318510-C-A': '0 (None)', '5-1331866-G-C': '0.000165 (European (Non-Finnish))', '5-1344443-G-A': '0 (None)', '5-1334369-A-T': '0 (None)', '5-1330356-A-G': '0 (None)', '5-1322960-TA-T': '0 (None)', '5-1320757-C-T': '0.000303 (European (Non-Finnish))', '5-1330371-T-C': '0 (None)', '5-1344770-G-A': '0 (None)', '5-1323884-G-A': '0 (None)', '5-1325939-G-A': '0 (None)', '5-1331865-A-G': '7.1e-05 (Latino)', '5-1334390-G-A': '0.000744 (African)', '5-1341990-T-C': '0.005829 (East Asian)', '5-1318538-G-A': '9.4e-05 (East Asian)', '5-1341919-T-C': '0 (None)', '5-1325878-C-G': '0 (None)', '5-1321804-G-C': '0 (None)', '5-1320719-A-T': '0 (None)', '5-1322998-C-T': '3.9e-05 (European (Non-Finnish))', '5-1344544-C-T': '0 (None)', '5-1344843-G-A': '0.02353 (African)', '5-1318520-G-T': '0 (None)', '5-1323895-C-T': '0 (None)', '5-1321798-A-G': '0 (None)', '5-1321851-G-A': '4.9e-05 (South Asian)', '5-1344445-C-T': '0 (None)', '5-1334431-C-T': '2.1e-05 (South Asian)', '5-1323958-C-T': '3.4e-05 (African)', '5-1321846-G-C': '0 (None)', '5-1339114-C-T': '8.7e-05 (European (Non-Finnish))', '5-1344999-C-T': '0 (None)', '5-1321837-A-AGGAGACG': '0 (None)', '5-1334360-AG-A': '0.000286 (South Asian)', '5-1344772-C-T': '0 (None)', '5-1331908-G-A': '0 (None)', '5-1341735-G-A': '0.006933 (African)', '5-1330411-A-G': '0.000561 (South Asian)', '5-1330404-G-A': '0 (None)', '5-1344458-G-T': '0 (None)', '5-1335160-T-G': '0.000173 (Latino)', '5-1323929-T-C': '4.9e-05 (European (Non-Finnish))', '5-1344579-G-A': '3.7e-05 (African)', '5-1341743-G-C': '5e-06 (European (Non-Finnish))', '5-1335133-G-A': '1.3e-05 (European (Non-Finnish))', '5-1330515-C-T': '3e-05 (Latino)', '5-1335121-G-A': '0.003789 (East Asian)', '5-1338119-C-T': '0 (None)', '5-1341851-G-T': '5e-06 (European (Non-Finnish))', '5-1325825-T-G': '5e-06 (European (Non-Finnish))', '5-1344814-G-A': '0 (None)', '5-1320766-G-A': '4e-05 (European (Non-Finnish))', '5-1323966-A-G': '0 (None)', '5-1321710-GCT-G': '0 (None)', '5-1344777-G-C': '0 (None)', '5-1338079-G-C': '0 (None)', '5-1331935-T-C': '0 (None)', '5-1325874-C-T': '0.000839 (European (Non-Finnish))', '5-1335152-C-G': '0 (None)', '5-1330386-G-A': '0.000243 (South Asian)', '5-1338937-C-T': '0 (None)', '5-1339034-C-T': '0 (None)', '5-1325920-C-T': '0 (None)', '5-1341861-C-T': '0 (None)', '5-1332023-A-T': '0 (None)', '5-1341787-T-C': '2e-05 (European (Non-Finnish))', '5-1324882-G-A': '0 (None)', '5-1339088-G-A': '0 (None)', '5-1334526-T-C': '0 (None)', '5-1344507-G-C': '0.000141 (European (Non-Finnish))', '5-1334464-T-C': '0 (None)', '5-1339128-G-A': '5e-06 (European (Non-Finnish))', '5-1331954-C-G': '0 (None)', '5-1339110-G-A': '0 (None)', '5-1324883-T-C': '5e-06 (European (Non-Finnish))', '5-1331978-G-A': '4.9e-05 (South Asian)', '5-1331966-G-T': '0 (None)', '5-1344830-T-C': '0 (None)', '5-1321959-C-T': '4.4e-05 (Latino)', '5-1325970-G-A': '0 (None)', '5-1318527-T-A': '5e-06 (European (Non-Finnish))', '5-1338092-T-G': '0 (None)', '5-1334393-G-T': '0 (None)', '5-1338037-G-A': '0 (None)', '5-1330454-G-A': '0 (None)', '5-1339061-T-A': '5e-06 (European (Non-Finnish))', '5-1341888-C-T': '4.9e-05 (South Asian)', '5-1334384-C-T': '0.00012 (South Asian)', '5-1321974-C-T': '6.2e-05 (South Asian)', '5-1344520-T-C': '0 (None)', '5-1318467-G-A': '0.00012 (South Asian)', '5-1339079-C-T': '0 (None)', '5-1338033-C-A': '2e-05 (European (Non-Finnish))', '5-1324911-T-C': '0 (None)', '5-1323044-G-A': '0.000739 (African)', '5-1334488-C-A': '0.000772 (European (Non-Finnish))', '5-1330370-G-A': '0.001063 (European (Non-Finnish))', '5-1324968-G-A': '0.000384 (African)', '5-1323071-A-C': '0 (None)', '5-1334507-G-GA': '0.000547 (African)', '5-1341930-C-T': '0 (None)', '5-1344855-G-A': '0 (None)', '5-1321928-T-A': '5e-06 (European (Non-Finnish))', '5-1344895-A-G': '9e-06 (European (Non-Finnish))', '5-1318533-A-G': '0 (None)', '5-1321977-G-A': '0 (None)', '5-1321844-G-A': '0.000175 (European (Non-Finnish))', '5-1332030-TCTC-T': '0.02489 (European (Non-Finnish))', '5-1325860-T-A': '0 (None)', '5-1330346-G-A': '0.000904 (African)', '5-1325845-G-A': '0 (None)', '5-1321726-T-C': '0 (None)', '5-1325899-A-C': '0 (None)', '5-1344609-G-T': '0 (None)', '5-1330449-G-A': '0.000608 (South Asian)', '5-1334432-G-A': '0 (None)', '5-1322941-C-T': '0 (None)', '5-1330419-C-T': '0.000158 (South Asian)', '5-1318600-C-A': '0 (None)', '5-1318505-C-T': '3e-05 (Latino)', '5-1322988-T-C': '0 (None)', '5-1318479-G-A': '0 (None)', '5-1324921-G-A': '0 (None)', '5-1321908-T-C': '0 (None)', '5-1341988-A-C': '0 (None)', '5-1344612-A-G': '0 (None)', '5-1320869-G-A': '0 (None)', '5-1325916-T-TACAAACGATGAAAATATCC': '0 (None)', '5-1338112-C-A': '0 (None)', '5-1318585-G-A': '0 (None)', '5-1320762-C-T': '0 (None)', '5-1318549-G-A': '0 (None)', '5-1334448-T-C': '0 (None)', '5-1321733-C-T': '0 (None)', '5-1339063-G-A': '5e-06 (European (Non-Finnish))', '5-1324922-T-A': '0 (None)', '5-1318475-G-A': '0.001094 (African)', '5-1339117-T-A': '0 (None)', '5-1334364-C-T': '0.000464 (East Asian)', '5-1339118-C-T': '0.000496 (East Asian)', '5-1344809-G-A': '0 (None)', '5-1331902-C-T': '0 (None)', '5-1334423-A-G': '2.9e-05 (European (Non-Finnish))', '5-1330476-G-A': '0 (None)', '5-1334367-C-CA': '0 (None)', '5-1330416-C-T': '3e-05 (Latino)', '5-1325855-C-T': '5e-06 (European (Non-Finnish))', '5-1341867-C-T': '0 (None)', '5-1325920-C-CTAT': '0 (None)', '5-1338947-G-A': '0 (None)', '5-1325882-A-G': '4.9e-05 (European (Non-Finnish))', '5-1321977-G-C': '0.000518 (African)', '5-1320861-G-A': '0 (None)', '5-1338067-C-G': '0 (None)', '5-1334378-G-C': '0 (None)', '5-1330420-G-A': '0 (None)', '5-1344519-G-A': '0.000615 (African)', '5-1338126-C-G': '0 (None)', '5-1337994-A-G': '4.4e-05 (European (Non-Finnish))', '5-1324848-T-C': '0 (None)', '5-1330549-G-A': '0 (None)', '5-1323980-A-G': '0 (None)', '5-1341804-G-A': '0 (None)', '5-1337980-T-TCCCCCC': '0.01311 (African)', '5-1344423-G-A': '8.7e-05 (Latino)', '5-1338043-G-A': '1.8e-05 (European (Non-Finnish))', '5-1323990-G-T': '0 (None)', '5-1334446-G-A': '0 (None)', '5-1330484-A-C': '0 (None)', '5-1335157-G-A': '0.006018 (European (Non-Finnish))', '5-1318498-G-A': '0 (None)', '5-1337985-A-G': '0 (None)', '5-1325884-G-A': '0 (None)', '5-1334372-G-T': '0 (None)', '5-1325919-T-A': '0 (None)', '5-1341803-C-T': '0.001252 (East Asian)', '5-1325973-G-A': '3.4e-05 (African)', '5-1335334-C-T': '0.000259 (South Asian)', '5-1330527-G-C': '2.1e-05 (South Asian)', '5-1339091-A-G': '0 (None)', '5-1330527-G-A': '0 (None)', '5-1335150-G-A': '0.000734 (African)', '5-1325875-G-A': '9.4e-05 (East Asian)', '5-1335217-A-G': '4.9e-05 (South Asian)', '5-1322989-C-T': '5e-06 (European (Non-Finnish))', '5-1341989-A-G': '1.6e-05 (European (Non-Finnish))', '5-1344458-G-A': '0.4788 (African)', '5-1341902-C-T': '0 (None)', '5-1335158-T-A': '5e-06 (European (Non-Finnish))', '5-1344903-G-A': '0 (None)', '5-1338963-G-T': '0 (None)', '5-1339052-C-T': '0 (None)', '5-1334517-C-T': '0.001644 (Latino)', '5-1341779-C-T': '0 (None)', '5-1344827-G-A': '0.000188 (European (Non-Finnish))', '5-1339169-C-T': '0 (None)', '5-1324961-G-A': '0 (None)', '5-1344879-G-A': '0.000173 (African)', '5-1341786-C-T': '0 (None)', '5-1320688-C-G': '0 (None)', '5-1341862-A-T': '2.1e-05 (South Asian)', '5-1321699-G-C': '5e-06 (European (Non-Finnish))', '5-1344759-C-A': '0.001729 (South Asian)', '5-1338065-G-C': '0 (None)', '5-1321976-GGCTGCCACATCTACGCACAGACGGCACTCACGAGGTGTGGAGGGCCGA-G': '0 (None)', '5-1324913-C-T': '0 (None)', '5-1335158-T-C': '0 (None)', '5-1323889-T-G': '5e-06 (European (Non-Finnish))', '5-1323972-A-G': '0 (None)', '5-1321976-G-A': '3.2e-05 (European (Non-Finnish))', '5-1341903-G-A': '5e-06 (European (Non-Finnish))', '5-1320685-C-T': '0.01568 (African)', '5-1321757-G-A': '2.1e-05 (South Asian)', '5-1330421-G-A': '2e-05 (European (Non-Finnish))', '5-1341954-T-G': '0 (None)', '5-1318602-C-G': '0 (None)', '5-1325942-A-G': '0 (None)', '5-1331933-G-A': '0 (None)', '5-1339019-A-G': '0.00075 (African)', '5-1341748-G-A': '0.006343 (South Asian)', '5-1321750-C-T': '0 (None)', '5-1325936-G-A': '0 (None)', '5-1320784-C-T': '0 (None)', '5-1344614-G-A': '0 (None)', '5-1344867-G-A': '0.000314 (African)', '5-1334410-C-T': '0.000284 (Latino)', '5-1344963-C-G': '0 (None)', '5-1330546-C-T': '0.000134 (European (Non-Finnish))', '5-1335196-C-T': '0 (None)', '5-1338054-T-C': '0 (None)', '5-1330405-G-A': '5e-06 (European (Non-Finnish))', '5-1325841-T-G': '0 (None)', '5-1318508-G-A': '0 (None)', '5-1321955-C-T': '0 (None)', '5-1334377-C-T': '5e-06 (European (Non-Finnish))', '5-1334424-A-T': '2.9e-05 (European (Non-Finnish))', '5-1344805-G-A': '0 (None)', '5-1318520-G-A': '2e-05 (European (Non-Finnish))', '5-1321970-G-A': '0 (None)', '5-1335240-T-C': '5e-06 (European (Non-Finnish))', '5-1324018-C-T': '0 (None)', '5-1325848-A-AT': '2.9e-05 (European (Non-Finnish))', '5-1323885-C-T': '2.1e-05 (South Asian)', '5-1338944-C-A': '0 (None)', '5-1321839-G-A': '0 (None)', '5-1344968-G-A': '0 (None)', '5-1339017-T-C': '0 (None)', '5-1318457-C-T': '1.2e-05 (European (Non-Finnish))', '5-1331940-CTCT-C': '5e-06 (European (Non-Finnish))', '5-1337987-C-A': '0 (None)', '5-1321951-A-C': '0 (None)', '5-1325833-G-T': '0 (None)', '5-1341917-T-C': '0 (None)', '5-1321836-C-G': '5e-06 (European (Non-Finnish))', '5-1324853-G-A': '0 (None)', '5-1325938-G-A': '9.4e-05 (East Asian)', '5-1341972-T-C': '0 (None)', '5-1323955-G-A': '0 (None)', '5-1334369-A-C': '0.000242 (South Asian)', '5-1344492-G-C': '0 (None)', '5-1335275-G-A': '0 (None)', '5-1324914-G-A': '0 (None)', '5-1320880-G-A': '0.003088 (East Asian)', '5-1335313-G-C': '0 (None)', '5-1321963-G-A': '4e-05 (European (Non-Finnish))', '5-1339148-T-C': '6e-06 (European (Non-Finnish))', '5-1334419-AAAG-A': '0 (None)', '5-1341794-C-G': '0 (None)', '5-1342000-T-C': '0.000148 (European (Non-Finnish))', '5-1335262-G-A': '0 (None)', '5-1338142-A-C': '0 (None)', '5-1338052-G-T': '0 (None)', '5-1323936-C-G': '0 (None)', '5-1325943-A-G': '0.00016 (South Asian)', '5-1331869-C-T': '0 (None)', '5-1341866-G-A': '4.9e-05 (South Asian)', '5-1334416-G-C': '0 (None)', '5-1339050-G-A': '4.9e-05 (South Asian)', '5-1344529-G-T': '0.000229 (Latino)', '5-1338987-C-T': '0 (None)', '5-1332045-A-G': '0 (None)', '5-1322994-T-C': '0 (None)', '5-1337980-T-TCCCCCCCCCCC': '0.000367 (African)', '5-1330516-G-A': '0.006798 (European (Non-Finnish))', '5-1332008-A-G': '0 (None)', '5-1344905-C-T': '0 (None)', '5-1320860-C-T': '0 (None)', '5-1344856-C-T': '0.003502 (South Asian)', '5-1344876-C-G': '0 (None)', '5-1318506-G-A': '8.1e-05 (European (Non-Finnish))', '5-1335149-C-T': '0 (None)', '5-1323062-G-A': '0 (None)', '5-1335173-G-C': '0 (None)', '5-1334367-C-A': '0 (None)', '5-1331883-A-G': '0.000802 (East Asian)', '5-1335173-G-A': '0.000287 (South Asian)', '5-1321897-C-T': '5e-06 (European (Non-Finnish))', '5-1325978-G-A': '0 (None)', '5-1323043-AGG-A': '0 (None)', '5-1344861-G-A': '0 (None)', '5-1323945-C-T': '1.2e-05 (European (Non-Finnish))', '5-1344577-G-A': '0 (None)', '5-1325969-C-T': '0 (None)', '5-1337999-C-T': '0.000275 (East Asian)', '5-1341742-C-G': '0 (None)', '5-1331906-G-A': '0 (None)', '5-1325957-T-C': '0 (None)', '5-1341736-T-A': '3.4e-05 (African)', '5-1335245-G-A': '0 (None)', '5-1330534-G-C': '0 (None)', '5-1323955-G-T': '0 (None)', '5-1334354-C-T': '0 (None)', '5-1318491-G-A': '0.02429 (European (Non-Finnish))', '5-1321962-G-T': '2.5e-05 (South Asian)', '5-1324031-C-T': '0 (None)', '5-1344782-C-T': '0 (None)', '5-1321894-G-C': '3.9e-05 (European (Non-Finnish))', '5-1321856-G-T': '0 (None)', '5-1344553-G-A': '0 (None)', '5-1332018-C-T': '0 (None)', '5-1335257-G-A': '0 (None)', '5-1321884-A-T': '0 (None)', '5-1341743-G-A': '3e-05 (South Asian)', '5-1320826-A-G': '0 (None)', '5-1334361-GC-G': '0 (None)', '5-1331895-C-T': '0 (None)', '5-1344825-C-T': '2.7e-05 (European (Non-Finnish))', '5-1339062-C-T': '0 (None)', '5-1321850-C-T': '0.01961 (South Asian)', '5-1335226-G-A': '0 (None)', '5-1341744-G-A': '3e-05 (South Asian)', '5-1324832-T-C': '0.000118 (Latino)', '5-1324840-G-T': '0 (None)', '5-1324024-C-T': '3.2e-05 (Latino)', '5-1321871-C-T': '0 (None)', '5-1335131-A-C': '0 (None)', '5-1321782-C-T': '0 (None)', '5-1344513-G-C': '0 (None)', '5-1321756-G-C': '0 (None)', '5-1335162-C-T': '0 (None)', '5-1344468-T-C': '0 (None)', '5-1318466-C-T': '5e-06 (European (Non-Finnish))', '5-1339097-C-T': '0 (None)', '5-1323908-T-C': '0 (None)', '5-1320822-C-T': '0.000126 (African)', '5-1338079-G-A': '0 (None)', '5-1320704-C-T': '0.04027 (European (Non-Finnish))', '5-1344759-C-T': '0 (None)', '5-1334380-C-G': '0 (None)', '5-1331931-C-A': '0 (None)', '5-1341913-A-C': '0 (None)', '5-1335179-C-T': '9.4e-05 (European (Non-Finnish))', '5-1338137-C-A': '0 (None)', '5-1318600-C-T': '0 (None)', '5-1322993-G-A': '0.01155 (African)', '5-1334521-C-G': '0 (None)', '5-1330522-G-A': '0 (None)', '5-1325852-C-T': '5.9e-05 (European (Non-Finnish))', '5-1344867-G-C': '0 (None)', '5-1344437-T-C': '0 (None)', '5-1318510-C-T': '0.000133 (African)', '5-1335290-CTGA-C': '0 (None)', '5-1344602-A-C': '0 (None)', '5-1334457-CA-C': '0 (None)', '5-1338975-A-G': '0 (None)', '5-1335176-C-T': '0.0171 (African)', '5-1334399-C-T': '0 (None)', '5-1338964-G-A': '0 (None)', '5-1318504-G-A': '0.000328 (South Asian)', '5-1339115-G-A': '0 (None)', '5-1339059-G-A': '0 (None)', '5-1339082-A-C': '0 (None)', '5-1318593-C-G': '0 (None)', '5-1344536-G-A': '0 (None)', '5-1321938-C-A': '0 (None)', '5-1332015-C-T': '0 (None)', '5-1321746-T-C': '0 (None)', '5-1341961-G-A': '0 (None)', '5-1323044-G-T': '0 (None)', '5-1344761-A-C': '0.005655 (African)', '5-1331890-C-A': '0.04213 (African)', '5-1321740-T-C': '0.000211 (European (Non-Finnish))', '5-1335280-G-A': '0.002711 (European (Non-Finnish))', '5-1323925-T-G': '0 (None)', '5-1344605-C-A': '0.001285 (Latino)', '5-1338946-C-T': '0.007413 (African)', '5-1344538-T-C': '2.1e-05 (South Asian)', '5-1341857-T-A': '0.000226 (Latino)', '5-1323042-AAGG-A': '0.000158 (South Asian)', '5-1338950-G-A': '3.6e-05 (African)', '5-1320800-A-G': '0 (None)', '5-1335135-C-T': '0.00052 (African)', '5-1344478-G-T': '0 (None)', '5-1339049-C-T': '3.4e-05 (African)', '5-1331879-G-C': '0.000603 (African)', '5-1322973-G-A': '0 (None)', '5-1331898-C-T': '3.4e-05 (African)', '5-1321872-G-A': '0 (None)', '5-1335235-A-G': '0 (None)', '5-1338966-C-T': '0 (None)', '5-1322999-G-A': '0.000103 (European (Non-Finnish))', '5-1339149-G-A': '0 (None)', '5-1330488-G-C': '0 (None)', '5-1321861-C-A': '0 (None)', '5-1342004-T-C': '0 (None)', '5-1321734-C-T': '2.1e-05 (South Asian)', '5-1341814-T-A': '0 (None)', '5-1341764-A-G': '0.000373 (South Asian)', '5-1342026-T-C': '0 (None)', '5-1331984-G-A': '0 (None)', '5-1338078-C-T': '0.02034 (European (Non-Finnish))', '5-1332022-A-T': '0.000102 (East Asian)', '5-1341951-C-A': '5e-06 (European (Non-Finnish))', '5-1325837-G-T': '4.9e-05 (European (Non-Finnish))', '5-1334411-G-T': '0 (None)', '5-1338998-G-A': '0 (None)', '5-1339094-C-T': '0 (None)', '5-1344561-G-A': '0.000122 (South Asian)', '5-1337980-T-TCCCCCCCCC': '0.001262 (African)', '5-1341798-C-T': '0 (None)', '5-1318507-T-G': '0 (None)', '5-1324878-C-T': '5e-06 (European (Non-Finnish))', '5-1344550-G-A': '2.2e-05 (South Asian)', '5-1337986-G-A': '0 (None)', '5-1334367-C-T': '0.000159 (South Asian)', '5-1323043-A-G': '0 (None)', '5-1334359-G-A': '0 (None)', '5-1335194-G-A': '0.006269 (African)', '5-1325960-T-C': '0 (None)', '5-1335180-T-C': '0 (None)', '5-1323871-C-T': '0.008709 (East Asian)', '5-1318513-TCTC-T': '0 (None)', '5-1335139-C-A': '3.8e-05 (African)', '5-1322960-T-G': '1.2e-05 (European (Non-Finnish))', '5-1344579-G-C': '0 (None)', '5-1337982-G-T': '0 (None)', '5-1321918-A-G': '0 (None)', '5-1337982-G-C': '0.2277 (African)', '5-1318620-T-C': '0 (None)', '5-1323938-C-A': '5e-06 (European (Non-Finnish))', '5-1344835-T-G': '0 (None)', '5-1320696-C-T': '0 (None)', '5-1338961-G-T': '0 (None)', '5-1335308-C-G': '0.02211 (African)', '5-1318475-G-C': '0 (None)', '5-1338941-C-T': '0 (None)', '5-1321819-G-A': '0.000131 (African)', '5-1323035-GA-G': '0 (None)', '5-1321743-C-G': '0 (None)', '5-1330403-C-T': '5e-06 (European (Non-Finnish))', '5-1335337-C-A': '0 (None)', '5-1344444-G-A': '0.04769 (African)', '5-1341843-G-C': '0 (None)', '5-1335220-G-A': '0 (None)', '5-1331907-G-C': '0.000749 (African)', '5-1320717-G-A': '0 (None)', '5-1344457-C-T': '0 (None)'}
ob = collections.OrderedDict(sorted(b.items()))
allele_freq_dict = {}

for i in range(len(data)):
    allele_freq = data[i]['allele_freq']
    variant = data[i]["variant_id"]
    allele_freq_dict[variant] = allele_freq
o_allele_freq_dict =  collections.OrderedDict(sorted(allele_freq_dict.items()))


#Takes the race out of filter AF
'''
ob_no_num = {}
for lel in ob:
    race = ob[lel]
    race_edit = ''
    for i in range(len(race)):
        if race[i] == '(':
            race_edit = race[i:]
    ob_no_num[lel] = race_edit

ob_no_num_sorted = collections.OrderedDict(sorted(ob_no_num.items()))
for value in ob_no_num_sorted.values():
    pprint(value)
'''

#Writes data to excel sheet
'''
workbook = xlsxwriter.Workbook('datalel3.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for key in ob.keys():

    worksheet.write(row,col,key)
    worksheet.write(row,col+1, ob[key])
    row += 1

row = 0
col = 2
for key in o_allele_freq_dict.keys():
    worksheet.write(row,col,o_allele_freq_dict[key])
    row += 1
workbook.close()
'''
