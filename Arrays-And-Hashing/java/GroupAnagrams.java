class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groupedAnagrams = new HashMap<>();

        for(String curString : strs) {
            int[] count = new int[26];
            for(char c : curString.toCharArray()){
                count[c - 'a']++;
            }
            String key = Arrays.toString(count);
            groupedAnagrams.putIfAbsent(key, new ArrayList<String>());
            groupedAnagrams.get(key).add(curString);
        }
        return new ArrayList<>(groupedAnagrams.values());
    }
}