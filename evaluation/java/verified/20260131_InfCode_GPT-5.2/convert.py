def read_jsonl() :
    import json

    data = []
    with open('/root/submit/experiments/evaluation/java/verified/20260131_InfCode_GPT-5.2/all_preds_old.jsonl', 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return data


def write_jsonl(data) :
    import json

    with open('/root/submit/experiments/evaluation/java/verified/20260131_InfCode_GPT-5.2/all_preds.jsonl', 'w') as file:
        for item in data:
            file.write(json.dumps(item) + '\n')


if __name__ == "__main__" :
    data = read_jsonl()
    new = []
    for d in data :
        owner = d['org']
        repo = d['repo']
        num = d['number']
        new.append({
            "model_name_or_path": "GPT-5.2",
            "instance_id": f'{owner}__{repo}-{num}',
            "model_patch": d["fix_patch"]
        }
        )
    write_jsonl(new)