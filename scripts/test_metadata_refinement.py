import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_clean_keywords(raw_text):
    """Extract clean keywords without stray brackets or broken terms."""
    if not raw_text:
        return []
    
    # Extract markdown link anchor texts: [term](url)
    link_keywords = re.findall(r'\[([^\]]+)\]\(.*?\)', raw_text)
    if link_keywords:
        kw_candidates = link_keywords
    else:
        # Fallback: split by comma or semicolon
        kw_candidates = re.split(r'[,;]', raw_text)

    clean_keywords = []
    for kw in kw_candidates:
        # Strip leading/trailing brackets, quotes, spaces
        k = kw.strip().strip('[]"\'` \t\n\r')
        if k and k not in clean_keywords:
            clean_keywords.append(k)

    return clean_keywords

# Test on problematic string
test_str = "[matrix, index notation for m by n](http://dlmf.nist.gov/search/search?q=matrix%2C%20index%20notation%20for%20m%20by%20n) , [definition](http://dlmf.nist.gov/search/search?q=definition)"
print("Test Raw:", test_str)
print("Test Cleaned:", extract_clean_keywords(test_str))
