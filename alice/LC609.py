class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """

        mapping = {}

        for one_dir in paths:
            li = one_dir.split(' ')
            path = li[0]
            for one_file in li[1:]:
                file_name, file_content = self.split_name_content(one_file)
                temp = mapping.get(file_content, [])
                temp.append(path + '/' + file_name)
                mapping[file_content] = temp

        return [x for x in mapping.values() if len(x) > 1]


    def split_name_content(self, file):
        file_name = ''
        file_content = ''
        content_flag = False

        for s in file:
            if s == '(':
                content_flag = True
                continue
            elif s == ')':
                return file_name, file_content
            else:
                if not content_flag:
                    file_name += s
                else:
                    file_content += s