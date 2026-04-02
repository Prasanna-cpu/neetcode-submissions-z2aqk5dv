class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        unique_cards = sorted(count)

        for card in unique_cards:
            occur = count[card]
            if occur > 0:
                for i in range(card , card+groupSize):
                    if count[i] < occur:
                        return False
                    count[i] -= occur
        return True